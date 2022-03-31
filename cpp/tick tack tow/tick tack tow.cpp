// tick tack tow.cpp : Defines the entry point for the application.
//

#include "tick tack tow.h"

using namespace std;

char board_arry[3][3] = { {55,56,57},
						 {52,53,54},
						 {49,50,51}, };

char board_arry_win_lookup[15][3] = { 
						 {42,56,57},
						 {52,42,54},
						 {49,50,42},

						 {55,56,42},
						 {52,42,54},
						 {42,50,51}, 

                         {42,42,42},
						 {52,53,54},
						 {49,50,51}, 

						 {55,56,57},
						 {42,42,42},
						 {49,50,51}, 

						 {55,56,57},
						 {52,53,54},
						 {42,42,42}, };
int in;

int define_display_board() {
	for (size_t y = 0; y < 3; y++)
	{
		for (size_t x = 0; x < 3; x++)
		{

			cout << " | " << board_arry[y][x] << " | ";
		}
		cout << endl;
	}
	return 0;
}
int get_user_input() {
	cin >> in;

	char c = '0' + in;

	for (size_t y = 0; y < 3; y++)
	{
		for (size_t x = 0; x < 3; x++)
		{
			if (c == board_arry[y][x])
			{
				cout << x <<" : " << y << "   " << board_arry[y][x] << " true" << endl;
				board_arry[y][x] = 'O';
			}
			else {
				cout << x << " : " << y << "   " << board_arry[y][x] << " false" << endl;
			}
			
		}
		cout << endl;
	}


	return 0;
}
int test(char play_indacator, int index_x, int index_y) {

	for (size_t y = 0; y < 3; y++)
	{
		for (size_t x = 0; x < 3; x++)
		{
			if (play_indacator == board_arry[y][x])
			{
				cout << x << " : " << y << "   " << board_arry[y + index_y][x + index_x] << " test true" << endl;
				
			}
			else {
				cout << x << " : " << y << "   " << board_arry[y][x] << " test flase" << endl;
			}

		}
		cout << endl;
	}

	return 0;
}

bool borad_game_full(char d) {
	for (size_t y = 0; y < 3; y++)
	{
		for (size_t x = 0; x < 3; x++)
		{
			if (d == board_arry[y][x])
			{
				return false;
			}
			else {
				return true;
			}

		}
		
	}
}

int main()
{
	bool meep;
	cout << "Hello CMake." << endl;
	define_display_board();
	while (true)
	{
		get_user_input();
		meep = borad_game_full('O');
		cout << meep << endl;
		test('O', 4,0);
		define_display_board();
	}
	return 0;
}
