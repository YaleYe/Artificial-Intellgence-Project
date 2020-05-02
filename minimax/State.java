import java.util.ArrayList;
class State{

    //represent state 
    ArrayList<Card> hand;
    ArrayList<Card> playedCards;
    Card trump;
    int tricks1;
    int tricks2;
    boolean playerOneWins = false;
    boolean playerTwoWins = false;
    int counter = 0;
    public State(ArrayList<Card> hand, ArrayList<Card> playedCards, Card trump, int tricks1, int tricks2) {
        this.hand = hand;
        this.playedCards = playedCards;
        this.trump = trump;
        this.tricks1 = tricks1;
        this.tricks2 = tricks2;
    }


    public void init(State state){
        state.hand = new ArrayList<Card>();
        state.playedCards = new ArrayList<Card>();
        state.tricks1 = 0;
        state.tricks2 = 0;
    }

    // if player wins 4 tricks, reach terminal state
    public boolean isGameOver(State state) {
        boolean gameOver = false;
        if (state.tricks1 >= 4) {
            // min wins
            state.playerOneWins = true;
            gameOver = true;
        } else if (tricks2 >= 4) {
            // max wins
            state.playerTwoWins = true;
            gameOver = true;
        }
        return gameOver;
    }

    public void increaseCounter(){
        counter += 1;
    }

    public int returnPlayerOneCounter(){
        return counter;

    }
    public int getCurrentLayer(){
        return counter;
    }

    public boolean PlayerOneWins(){
        return playerOneWins;
    }

    public boolean PlayerTwoWins() {
        return playerTwoWins;
    }

}

