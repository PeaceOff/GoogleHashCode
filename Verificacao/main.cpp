#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;
int minIng;
int maxCells;

void debugInput(int rows, int  cols, int  minIng, int maxCells,vector<vector<char>> pizza) {

	cout << "Debugging Input" << endl;
	cout << "Rows : " << rows << " | Cols : " << cols << " | MinIng : " << minIng << " | MaxCells : " << maxCells << endl;
	for (int r = 0; r < rows; r++) {
		for (int c = 0; c < cols; c++) {
			cout << pizza[r][c];
		}
		cout << endl;
	};
	return;
}

bool checkSlice(int xi, int yi, int xf, int yf, vector<vector<char>>* pizza, vector<vector<bool>>* checkVec) {
	
	//Return true if valid
	int tomatoeCount = 0;
	int mushroomCount = 0;
	int counter = 0;
	for (int x = xi; x <= xf; x++){
		for (int y = yi; y <= yf; y++) {
			if ((*checkVec)[x][y]) {
				return false;
			}
			(*checkVec)[x][y] = true;

			counter++;

			if ((*pizza)[x][y] == 'T') {
				tomatoeCount++;
			}
			else {
				mushroomCount++;
			}
		}
	};
	
	if (counter > maxCells)
		return false;
	
	if (tomatoeCount < minIng || mushroomCount < minIng)
		return false;
	
	return true;
}

int main() {
	ifstream inputFile;
	ifstream outputFile;
	string iFileName;
	string oFileName;

	//Input data---------------------------------------------------------------------------------------
	vector<vector<char>> pizza;
	vector<vector<bool>> checkVec;
	int rows, cols;

	cout << "Input File [Same directory with extension]: ";
	cin >> iFileName;
	
	cout << "Opening File..." << endl;
	inputFile.open(iFileName);

	if (inputFile.is_open()) {
		//Read Integers
		cout << "Reading Data..." << endl;
		inputFile >> rows;
		inputFile >> cols;
		inputFile >> minIng;
		inputFile >> maxCells;

		//Limpar o resto da primeira linha
		string lixo;
		getline(inputFile, lixo);

		//Read Pizza
		for (int x = 0; x < rows; x++) {
			
			string line;
			getline(inputFile,line);
			vector<char> l;
			vector<bool> ll;
			
			for (int y = 0; y < cols; y++) {
			
				l.push_back(line[y]);
				ll.push_back(false);
			
			}

			pizza.push_back(l);
			checkVec.push_back(ll);
		}
	}
	else {
		cout << "Could not read file!" << endl;
		system("pause");
		return -1;
	}

	debugInput(rows, cols, minIng, maxCells, pizza);

	cout << "Data Read, Closing File..." << endl;
	inputFile.close();

	//Output data-------------------------------------------------------------------------------
	cout << "Output File [Same directory with extension]: ";
	cin >> oFileName;

	cout << "Opening File..." << endl;
	outputFile.open(oFileName);

	int nSlices, nOccupied;

	if (outputFile.is_open()) {
		//Read Integers
		cout << "Reading Data..." << endl;
		outputFile >> nSlices;
		cout << "NSlices : " << nSlices << endl;

		//Limpar o resto da primeira linha
		string lixo;
		getline(outputFile, lixo);

		stringstream ss;
		string line;

		while (nSlices) {
			//Read Slice
			line.clear();
			getline(outputFile, line);
			ss.clear();
			ss << line;
			int xi, yi, xf, yf;
			ss >> xi >> yi >> xf >> yf;
			cout << "Read : " << xi << " " << yi << " " << xf << " " << yf << endl;

			if (!checkSlice(xi, yi, xf, yf, &pizza, &checkVec)) {
				
				cout << "Invalid Result! at " << xi << ";" << yi << ";" << xf << ";" << yf << endl;
				outputFile.close();
				system("pause");
				return -1;

			};
			nSlices--;
		}
	}
	else {
		cout << "Could not read file!" << endl;
		system("pause");
		return -1;
	}

	cout << "Data Read, Closing File..." << endl;
	outputFile.close();
	cout << "Everything seems alright!" << endl;
	system("pause");
	return 0;
}