#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

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

int main() {
	ifstream inputFile;
	ifstream outputFile;
	string iFileName;
	string oFileName;

	//Input data
	vector<vector<char>> pizza;
	int rows, cols, minIng, maxCells;

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

		//Read Pizza
		for (int x = 0; x < rows; x++) {
			char* line = (char*)malloc(sizeof(char) * cols);
			inputFile.getline(line,cols);
			for (int y = 0; y < cols; y++) {
				pizza[x][y] = line[y];
			}
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
	
	//todo

	//Output data

	return 0;
}