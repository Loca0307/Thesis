
int main() {
    string filename;
    cout << "Enter the filename: ";
    cin >> filename;

    ifstream userfile(filename);
    if (!userfile) {
        cerr << "Error opening file." << endl;
        return 1;
    }
    int N, type;
    userfile >> N >> type;

    if (type== 0) {
        Matrix<int> A(N), B(N);
        A.readfile(userfile);
        B.readfile(userfile);
    
        cout << "Matrix A:\n"; A.print();
        cout << "Matrix B:\n"; B.print();
        cout << "A + B:\n"; (A + B).print();
        cout << "A * B:\n"; (A * B).print();
        cout << "Diagonal sum of A: " << A.diagonalSum() << endl;
        cout << "Diagonal sum of B: " << B.diagonalSum() << endl;
        cout << "Swapping rows 0 and 1 in A:\n"; A.swaprows(0, 1); A.print();
        cout << "Swapping columns 0 and 1 in A:\n"; A.swapcols(0, 1); A.print();
        cout << "Changing value at (0, 0) in A to 348:\n"; A.chngevalue(0, 0, 348); A.print();
        }   else if (type == 1) {
            Matrix<double> A(N), B(N);
            A.readfile(userfile);
            B.readfile(userfile);

            cout << "Matrix A:\n"; A.print();
            cout << "Matrix B:\n"; B.print();
            cout << "A + B:\n"; (A + B).print();
            cout << "A * B:\n"; (A * B).print();
            cout << "Diagonal sum of A: " << A.diagonalSum() << endl;
            cout << "Diagonal sum of B: " << B.diagonalSum() << endl;
            cout << "Swapping rows 0 and 1 in A:\n"; A.swaprows(0, 1); A.print();
            cout << "Swapping columns 0 and 1 in A:\n"; A.swapcols(0, 1); A.print();
            cout << "Changing value at (0, 0) in A to 348.843:\n"; A.chngevalue(0, 0, 349.843); A.print();

        }
        userfile.close(); 
        return 0;
    }