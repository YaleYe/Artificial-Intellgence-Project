;problem 1
;Initial state
; At(Monkey, A) ^ At(Bananas,B) ^ At(Box,C) ^ Height(Monkey,Low) ^ Height(Box, Low) ^ Height(Bananas,High) ^ Pushable(Box) ^ Climbale(Box)

;Actions:

; Go(x,y)    Precond: at(Monkey,x)
;            Effect: at(Monkey,x), !at(Monkey,x)

;Push(b,x,y) Precond: at(Monkey,x), at(b,x), Pushable(b)
;            Effect: at(b,y), at(Monkey,y), !at(Monkey,x), !at(b,x)

;ClimbUp(b)  Precond: at(Monkey,x), at (b,x), Climbable(b)
;            Effect: On(Monkey,b), !Height(Monkey, Low), Height(Monkey, High)

;Grasp(o)    Precond: Height(Monkey,h), Height(o,h), at(Monkey,x), at(o,x)
;            Effect: Have(Monkey,o)

;ClimbDown(b) Precond: at(Monkey,x), Height(Monkey,High)
;            Effect: !On(Monkey,b), !Height(Monkey,High), Height(Monkey,Low)

;UnGrasp(o)  Precond: Have(Monkey,o)
;            Effect: !Have(Monkey,o)

(define (problem monkey-bananas)
    (:domain monkey)
    (:predicates 
        (goto ?x ?y)
        (climb ?x)
        (pushBox ?x ?y)
        (grasp ?x)
        (at ?x ?y)
        (hasbananas)
        (onFloor)
        (onBox ?x))

    ;action goto
    (:action goto
            :parameters (?x ?y)
            :precondition (and  
                            (on-floor)
                            (at monkey ?y))
            :effect (and    
                        (at monkey ?x)
                        (not (at monkey ?y))
                        )
    )
    ;action climb
    (:action climb
            :parameters (?x)
            

            :precondition(and
                        (at box ?x)
                        (at monkey ?x)
            )

            :effect (and
                        (onBox ?y)
                        (at monkey ?y)
                        (onFloor)
            )
    )

    ;action grasp
    (:action grasp
            :parameters(?y)
            :precondition (and
                            (at Bananas ?y)
                            (onBox ?y)
                            )

            :effect (and
                        (hasbananas))
    )
)
    ;backward search
    ;start at the State of (hasbanana, onBox, at location of bananas)
    ;then climb down
    ;push the box at its old spot
    ;loop through (go to action) to find the original location
                            
  

-



    
    