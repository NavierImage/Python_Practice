#include <iostream>
#include <vector>

int main() {
	int n; int m; int block;

	std::cin >> n >> m >> block;
	
	int world[501][501];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			std::cin >> world[i][j];
		}
	}

	std::vector<int> result1;
	std::vector<int> result2;
	int bc = block;

	for (int h = 0; h < 257; h++) {
		int block = bc;
		int time = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (world[i][j] > h) {
					time += 2 * (world[i][j] - h);
					block += (world[i][j] - h);

				}

				else if (world[i][j] < h) {
					block -= h - world[i][j];
					time += h - world[i][j];

				}
				else {
					continue;
				}


			}
		}
		if (block < 0) {
			continue;
		}
		
		result1.push_back(time);
		result2.push_back(h);
	}	

	int settime = 99999999;
	int idx = -1;
	int setidx = 0;
	for (auto loop : result1) {
		idx += 1;
		if (settime >= loop) {
			settime = loop;
			setidx = idx;
		}
	}


	int iwanth = result2[setidx];

	std::cout << settime;
	std::cout << ' ';
	std::cout << iwanth;

}