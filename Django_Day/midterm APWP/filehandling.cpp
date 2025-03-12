#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

class Student {
public:
    string name;
    double score;

    Student(const string& name, double score) : name(name), score(score) {}
};

void readScores(const string& inputFile, double& averageScore, vector<Student>& students) {
    ifstream file(inputFile);
    int n;
    file >> n;  // Read the number of students

    double totalScore = 0;
    string name;
    double score;
    
    for (int i = 0; i < n; ++i) {
        file >> name >> score;
        students.emplace_back(name, score);
        totalScore += score;
    }
    
    averageScore = totalScore / n;
}

bool sortByName(const Student& a, const Student& b) {
    return a.name < b.name;  // Sort by name
}

bool sortByScore(const Student& a, const Student& b) {
    return a.score > b.score;  // Sort by score descending
}

void writeOutput(const string& outputFile, double averageScore, const vector<Student>& students) {
    ofstream file(outputFile);
    file << "Average Score: " << fixed << setprecision(2) << averageScore << endl;

    vector<Student> sortedByName = students;
    sort(sortedByName.begin(), sortedByName.end(), sortByName);

    vector<Student> sortedByScore = students;
    sort(sortedByScore.begin(), sortedByScore.end(), sortByScore);

    file << "\nStudents sorted by name:\n";
    for (const auto& student : sortedByName) {
        file << student.name << ": " << student.score << endl;
    }

    file << "\nStudents sorted by score:\n";
    for (const auto& student : sortedByScore) {
        file << student.name << ": " << student.score << endl;
    }
}

int main() {
    string inputFile = "input.txt";
    string outputFile = "output.txt";

    double averageScore;
    vector<Student> students;

    readScores(inputFile, averageScore, students);
    writeOutput(outputFile, averageScore, students);

    return 0;
}