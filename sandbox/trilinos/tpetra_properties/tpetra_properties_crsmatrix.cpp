#include "tpetra_properties_crsmatrix.h"

RCP<const Teuchos::Comm<int> > comm;

int main(int argc, char *argv[]) {
	
	//  General setup for Teuchos/communication
	Teuchos::GlobalMPISession mpiSession(&argc, &argv);
	Platform& platform = Tpetra::DefaultPlatform::getDefaultPlatform();
	comm = rcp (new Teuchos::MpiComm<int> (MPI_COMM_WORLD));	
	RCP<NT> node = platform.getNode();
	int myRank = comm->getRank();
	Teuchos::oblackholestream blackhole;
	std::ostream& out = (myRank == 0) ? std::cout : blackhole;
	RCP<Teuchos::FancyOStream> fos = Teuchos::fancyOStream(Teuchos::rcpFromRef(out));

	// Load and run tests on Matrix Market file
	std::string filename("../demo.mtx");
	RCP<MAT> A = Tpetra::MatrixMarket::Reader<MAT>::readSparseFile(filename, comm, node);
	runGauntlet(A);

}
void runGauntlet(RCP<MAT> &A) {
	// Test squareness
	if (A->getGlobalNumRows() != A->getGlobalNumCols() ) {
		std::cout << "Not a square matrix, exiting\n";
		exit(-1);
	}
	calcRowVariance(A);
	calcColVariance(A);
	calcDiagVariance(A);
	calcNonzeros(A);
	calcDim(A);
	calcFrobeniusNorm(A);
}

//  Return the maximum row variance for the matrix
//  The average of the squared differences from the Mean.
void calcRowVariance(RCP<MAT> &A) {
	LO localRows = A->getNodeNumRows(); 
	ArrayView<const ST> values;
	ArrayView<const LO> indices;
	GO numColsInCurrentRow;
	ST mean, variance, maxVariance = 0.0;

	//  Go through each row on the current process
	for (LO row = 0; row < localRows; row++) {
		mean = variance = 0.0; 
		numColsInCurrentRow = A->getNumEntriesInLocalRow(row); 
		A->getLocalRowView(row, indices, values); 

		//  Two-step approach for variance, could be more efficient 
		for (LO col = 0; col < numColsInCurrentRow; col++) {
			mean += values[col];
		} 
		//  Divide entries by the total number of columns (to include zeros)
		mean /= A->getGlobalNumCols();
		for (LO col = 0; col < numColsInCurrentRow; col++) {
			variance += (values[col] - mean) * (values[col] - mean);
		}
		variance /= A->getGlobalNumCols();
		if (variance > maxVariance) maxVariance = variance;
	}
	//  Communicate local results, compare
	double* results = new double[comm->getSize()];
	double max[] = {maxVariance};
	Teuchos::gather(max, 1, results, comm->getSize(), 0, *comm);
	if (comm->getRank() == 0) {
		for (int i = 0; i < comm->getSize(); i++) {
			if (results[i] > maxVariance) {
				maxVariance = results[i];
			}
		}
		std::cout << maxVariance << std::endl;
	}
}

//  Transpose the matrix, get row variance
void calcColVariance(RCP<MAT> &A) {
	Tpetra::RowMatrixTransposer<ST, LO, GO, NT> transposer(A);	
	RCP<MAT> B = transposer.createTranspose();
	calcRowVariance(B);
}

void calcDiagVariance(RCP<MAT> &A) {
	ST localMean, mean, variance, maxVariance = 0.0; //normal things
	typedef Tpetra::Map<LO, GO> map_type; //basic map setup
	const GO indexBase = 0; //idk
	GO numGlobalElements = A->getGlobalNumDiags(); //just need the space for diagonal entries
	RCP<const map_type> map = rcp(new map_type (numGlobalElements, indexBase, comm)); //map itself
	VEC v(map);

	A->getLocalDiagCopy(v);
	Teuchos::ArrayRCP<const ST> array = v.getData();	
	for (int i = 0; i < array.size(); i++) {
		localMean += array[i];	
	}
	Teuchos::reduceAll(*comm, Teuchos::REDUCE_SUM, 1, &localMean, &mean);
	mean /= A->getGlobalNumRows();
	for (int i = 0; i < array.size(); i++) {
		variance += (array[i] - mean) * (array[i] - mean);
	}	
	double result = 0;
	Teuchos::reduceAll(*comm, Teuchos::REDUCE_SUM, 1, &variance, &result);
	result /= A->getGlobalNumRows();
	std::cout << "result:" << result << std::endl;
}

void calcNonzeros(RCP<MAT> &A) {
	std::cout << A->getGlobalNumEntries();
}

void calcDim(RCP<MAT> &A) {
	std::cout << A->getGlobalNumRows() << ", " << std::endl;
}

//  Already implemented in Tpetra
void calcFrobeniusNorm(RCP<MAT> &A) {
	std::cout << A->getFrobeniusNorm() << ", " << std::endl;
}
void calcSymmetricFrobeniusNorm(RCP<MAT> &A){ }
void calcAntisymmetricFrobeniusNorm(RCP<MAT> &A){ }
void calcOneNorm(RCP<MAT> &A){ }
void calcInfNorm(RCP<MAT> &A){ }

void calcDiagAvg(RCP<MAT> &A) {
	ST mean, variance, maxVariance = 0.0; //normal things
	typedef Tpetra::Map<LO, GO> map_type; //basic map setup
	const GO indexBase = 0; //idk
	GO numGlobalElements = A->getGlobalNumDiags(); //just need the space for diagonal entries
	RCP<const map_type> map = rcp(new map_type (numGlobalElements, indexBase, comm)); //map itself
	VEC v(map);
	A->getLocalDiagCopy(v);
	std::cout << "avg:" << v.meanValue() << std::endl;
}

