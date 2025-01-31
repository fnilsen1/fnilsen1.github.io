#include "masterVisual.h"
#include "mastermind.h"
#include "utilities.h"

void playMastermindVisual()
{
	// BEGIN: 5
	constexpr int size = 4;
	constexpr int letters = 6;
	constexpr char startLetter = 'A';
	constexpr int maxTries = 6;

	
	bool playAgain = true;
	while (playAgain){
		MastermindWindow mwin{900, 20, winW, winH, size, "Mastermind"};
		string code = randomizeString(size, startLetter + letters - 1, startLetter );
		string guess;
		int round = 0;
		cout << "*** Mastermind ***" << endl;
		
		// Viser CODE. addGuess brukes til å vise den hemmelige koden med parameter round = 0
		addGuess(mwin, code, startLetter);
		mwin.setCodeHidden(true);
		
	
		while (round != maxTries) {
			cout << "Colors: a = red, b = green, c = yellow, d = blue, e = lilac, f = cyan" << endl;
			cout << "What's your guess? (" << size << " chars)" << endl;
			guess = mwin.getInput(size, startLetter + letters - 1, startLetter);
			cout << "Your guess: " << guess << endl;
			++round;
			if(mwin.should_close()) {
				break;
			}

			int correct = checkCharactersAndPosition(code, guess);
			int correctChars = checkCharacters(code, guess);

			// Det nyeste gjettet legges til i grafikkvinduet sammen med riktig tilbakemelding.
			addGuess(mwin, guess, startLetter);
			addFeedback(mwin, correct, correctChars);
			
			// Hopp ut av løkken dersom spiller har gjettet koden.
			if (correct == size) {
				break;
			}

			cout << "Correct characters: " << correctChars << endl
				 << "Correct positions: " << correct << endl << "You have " << maxTries - round
				 << " tries left." << endl << endl;
		}

		if (guess == code) {
			cout << "Congratulations, you cracked the code!" << endl;
		} else {
			cout << "You didn't manage to crack the code..." << endl;
		}
		mwin.drawGuessesAndFeedbacks();
		mwin.setCodeHidden(false);
		mwin.wait_for_close();
		
		playAgain = askYesNoQuestion("Do you want to play again?");
	}
	// END: 5 
}

void addGuess(MastermindWindow &mwin, const string code, const char startLetter)
{
	// BEGIN: 5b
	mwin.guesses.push_back({code, startLetter});
	// END: 5b
}

void addFeedback(MastermindWindow &mwin, const int correctPosition, const int correctCharacter)
{
	// BEGIN: 5e
	mwin.feedbacks.push_back({correctPosition, correctCharacter});
	// END: 5e
}

void MastermindWindow::drawCodeHider()
{
	if(code_hidden) {
		draw_rectangle(Point{padX, 3 * padY}, winW - size * padX, padY, Color::black);
	}
}

MastermindWindow::MastermindWindow(int x, int y, int w, int h, int size, const string &title) 
: AnimationWindow(x, y, w, h, title),
guessBtn{{upperLeftCornerBtn.x, upperLeftCornerBtn.y}, btnW, btnH, "Add"}, 
guess{{upperLeftCornerInBox.x, upperLeftCornerInBox.y}, inBoxW, inBoxH, ""},
size(size)
{
	add(guess);
	add(guessBtn);
	guessBtn.setCallback(std::bind(&MastermindWindow::cb_guess, this)); 
};

void MastermindWindow::drawGuessesAndFeedbacks()
{
	std::map<int, Color> colorConverter{
		{1, Color::red},
		{2, Color::green},
		{3, Color::yellow},
		{4, Color::blue},
		{5, Color::blue_violet},
		{6, Color::dark_cyan}};

	for (int guessIndex = 0; guessIndex < static_cast<int>(guesses.size()); guessIndex++)
	{
		// BEGIN: 5c
		// Legger til et gjett i grafikkvinduet i form av fargede rektangler.
		// xPos initialiseres likt hver gang denne funksjonen kalles, mens yPos er avhengig av round,
		// slik at gjetningene vises under hverandre.
		Guess guess = guesses.at(guessIndex);
		int xPos = padX;
		const int yPos = 3 * padY + 2 * padY * guessIndex;
		for (int i = 0; i < size; i++)
		{
			draw_rectangle(Point{xPos, yPos}, padX, padY, colorConverter.at(guess.code[i] - guess.startLetter + 1), Color::black);
			xPos += 2 * padX;
		}
		// END: 5c
	}

	for (int feedbackIndex = 0; feedbackIndex < static_cast<int>(feedbacks.size()); feedbackIndex++)
	{
		// BEGIN: 5f
		Feedback feedback = feedbacks.at(feedbackIndex);
		int xPos = 9 * padX + radCircle;
		const int yPos = 5.5 * padY + 2 * padY * (feedbackIndex);
		for (int i = 0; i < size; i++)
		{
			Color indicatorColour = Color::white;
			if (i < feedback.correctPosition)
			{
				indicatorColour = Color::black;
			}
			else if (i < (feedback.correctPosition + std::max<int>(0, feedback.correctCharacter - feedback.correctPosition)))
			{
				indicatorColour = Color::grey;
			}
			draw_circle(Point{xPos, yPos}, radCircle, indicatorColour, Color::black);

			xPos += 2 * radCircle;
		}
		// END: 5f
	}
}
string MastermindWindow::wait_for_guess()
{
	while (!button_pressed && !should_close())
	{
		drawGuessesAndFeedbacks();
		// Should be drawn last as it has to be on top
		drawCodeHider();

		next_frame();
	}
	button_pressed = false;
	string newGuess = guess.getText(); 
	guess.setText("");

	return newGuess;
}

string MastermindWindow::getInput(unsigned int n, char upper, char lower)
{
	bool validInput = false;
	string guess;
	while (!validInput && !should_close())
	{
		guess.clear();
		string input = wait_for_guess();
		if (input.size() == n)
		{
			for (unsigned int i = 0; i < n; i++)
			{
				char ch = input.at(i);
				if (isalpha(ch) && toupper(ch) <= upper && lower <= toupper(ch))
				{
					guess += toupper(ch);
				}
				else
					break;
			}
		}
		if (guess.size() == n)
		{
			validInput = true;
		}
		else
		{
			cout << "Invalid input guess again" << endl;
		}
	}
	return guess;
}

void MastermindWindow::setCodeHidden(bool hidden) {
	code_hidden = hidden;
}

