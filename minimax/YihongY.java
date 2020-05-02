import java.util.ArrayList;
import java.util.Collections;
import javax.xml.transform.TransformerConfigurationException;

//trumpCard is the 15card suit
public class YihongY{
    public static Player getPlayer(){ return new YihongYPlayer(); }


public static class YihongYPlayer implements Player{
    ArrayList<Card> hand;
    ArrayList<Card> playedCards;
    Card trump;
    State value;
 

    State state = new State(hand,playedCards,trump,0,0);

    // function MAX-VALUE(state) returns a utility value
    //if TERMINAL-TEST(state) then return UTILITY(state)
    //v ← −∞
    //for each a in ACTIONS(state) do
    //v ← MAX(v, MIN-VALUE(RESULT(s, a)))
    //return v

    public State maxValue(State state){
        if(state.isGameOver(state)){
            return state;}       
        
        //for each a in ACTIONS(state) do
        //add card from hands to played    
        for (Card tempCard : hand) {
            playedCards.add(tempCard);
            state.hand.remove(tempCard);
            state.counter += 1;
        }

        value = minValue(state);
        
            return value;}



    //  function MIN-VALUE(state) returns a utility value
    //if TERMINAL-TEST(state) then return UTILITY(state)
    //v ← ∞
    //for each a in ACTIONS(state) do
    //v ← MIN(v, MAX-VALUE(RESULT(s, a)))
    //return v

    public State minValue(State state){
        if(state.isGameOver(state)){
            state.counter += 1;
            return state;}
        
        for(Card tempCard : state.hand){
            //pick a ramdom card to play
            playedCards.add(tempCard);
            hand.remove(tempCard);


            //compare the playedCard with the card in deck
            //methods public boolean greater(Card c, Card trump) {
            if(tempCard.greater(state.playedCards.get(state.playedCards.size() - 1),state.trump)){
                state.tricks1 += 1;}
            else{
                state.tricks2 += 1;}}
            
    
        value = maxValue(state);
        return value;}


    

    public State minimax(State state){
        value = maxValue(state);
        return state;
    }
    //function ALPHA-BETA-SEARCH(state) returns an action
    //v ← MAX-VALUE(state,−∞,+∞)
    //return the action

 

    
    public Card playFirstCard(ArrayList<Card> hand, ArrayList<Card> playedCards, Card trump, int tricks1, int tricks2){
        if (hand.size() == 0) {
            return null;
        }
        State stateTemp = new State(hand, playedCards, trump, tricks1, tricks2);
        ArrayList<Integer> countWin = new ArrayList<Integer>();
        //menta carlo stimulation
        for(Card temp : playedCards){ //go through each card to check their win count
            int counter = 0;
            for (int i = 0; i < 1000; i++) {
                minimax(stateTemp);
                if(stateTemp.playerOneWins){
                    counter += 1;
                    stateTemp.increaseCounter();}
                stateTemp.init(stateTemp); //init the state and run it again
                }
            //loop is over save the player1 counter to countWin array
            countWin.add(counter);

        }
        // get index of the card wins the most round

        int highestWinableindex = Collections.max(countWin);
        return hand.get(highestWinableindex);

    }
    

	public Card playSecondCard(ArrayList<Card> hand, ArrayList<Card> playedCards, Card trump, int tricks1, int tricks2){
       if (hand.size() == 0) {
            return null;}

        State stateTemp = new State(hand, playedCards, trump, tricks1, tricks2);
        ArrayList<Integer> countWin = new ArrayList<Integer>();
        //menta carlo stimulation
        for(Card temp : playedCards){ //go through each card to check their win count
            int counter = 0;
            for (int i = 0; i < 1000; i++) {
                minimax(stateTemp);
                if(stateTemp.PlayerTwoWins()){
                    counter += 1;
                    stateTemp.increaseCounter();}
                stateTemp.init(stateTemp); //init the state and run it again
                }
            //loop is over save the player1 counter to countWin array
            countWin.add(counter);

        }
        // get the highest winnable card and play it

        int highestWinableindex = Collections.max(countWin);
        return hand.get(highestWinableindex);
    }
}
}

