#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <thread>

class Tank {
public:
    int damage;
    int hp;
    int armor;
    int price;
    int id;

    Tank(int d, int h, int a, int p, int i) : damage(d), hp(h), armor(a), price(p), id(i) {}
};

// Function to read tanks from the input file
std::vector<Tank> readTanksFromFile(const std::string &filename) {
    std::vector<Tank> tanks;
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file." << std::endl;
        return tanks;
    }

    int numTanks;
    file >> numTanks;
    for (int i = 0; i < numTanks; ++i) {
        int damage, hp, armor, price;
        file >> damage >> hp >> armor >> price;
        tanks.emplace_back(damage, hp, armor, price, i + 1);
    }

    file.close();
    return tanks;
}

// Function to sort tanks by price and damage
void sortTanks(const std::vector<Tank> &tanks, std::vector<Tank> &sortedByPrice, std::vector<Tank> &sortedByDamage) {
    sortedByPrice = tanks;
    sortedByDamage = tanks;

    // Sort by price
    std::sort(sortedByPrice.begin(), sortedByPrice.end(), [](const Tank &a, const Tank &b) {
        return (a.price < b.price) || (a.price == b.price && a.damage > b.damage);
    });

    // Sort by damage
    std::sort(sortedByDamage.begin(), sortedByDamage.end(), [](const Tank &a, const Tank &b) {
        return (a.damage > b.damage) || (a.damage == b.damage && a.price < b.price);
    });
}

// Function to write results to the output file
void writeResultsToFile(const std::vector<Tank> &tanksPrice, const std::vector<Tank> &tanksDamage, const std::string &outputFilename) {
    std::ofstream file(outputFilename);
    if (!file.is_open()) {
        std::cerr << "Error opening output file." << std::endl;
        return;
    }

    file << "Sorted by Price:\n";
    for (const auto &tank : tanksPrice) {
        file << tank.id << '\n';
    }

    file << "\nSorted by Damage:\n";
    for (const auto &tank : tanksDamage) {
        file << tank.id << '\n';
    }

    file.close();
}

// Function to process tanks
void processTanks(const std::string &inputFilename, const std::string &outputFilename) {
    auto tanks = readTanksFromFile(inputFilename);
    std::vector<Tank> tanksSortedByPrice;
    std::vector<Tank> tanksSortedByDamage;
    
    sortTanks(tanks, tanksSortedByPrice, tanksSortedByDamage);
    writeResultsToFile(tanksSortedByPrice, tanksSortedByDamage, outputFilename);
}

// Main function
int main() {
    std::string inputFile = "input.txt";
    std::string outputFile = "output.txt";

    // Create a thread to process tanks
    std::thread tankThread(processTanks, inputFile, outputFile);
    tankThread.join();  // Wait for the thread to finish

    std::cout << "Tank processing completed. Results written to " << outputFile << "." << std::endl;
    return 0;
}