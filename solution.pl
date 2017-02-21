:- use_module(library(clpfd)).
:- use_module(library(lists)).
%open(file,mode,var).
%rect(X,Length,Y,Height)
%disjoint2(Rectangles)



solve(Pizza, R, C, L, H, Vars) :-
    MinSliceSize is 2*L,
    TotalArea is R*C,
    MaxSlices is floor(TotalArea / MinSliceSize),

    buildDomainVariables(1, MaxSlices, R, C, H, Vars, AreaOccupied),
    AreaOccupied #=< TotalArea,

    buildRectangles(Vars, Rectangles),
    disjoint2(Rectangles),                          % each cell of the pizza must be included in at most one slice

    minimumIngredients(Pizza, R, C, L, H, Vars),    % each slice must contain at least L cells of mushroom and L cells of tomato

    labeling([ff, time_out(20000, _), maximize(AreaOccupied)], Vars),
    printSolution(Vars).


buildDomainVariables(MaxSlices, MaxSlices, _, _, _, [], 0).
buildDomainVariables(N, MaxSlices, R, C, H, [Xi, Length, Yi, Height | Vars], AreaOccupied) :-
    domain([Xi], 1, C),
    domain([Length], 0, C),
    domain([Yi], 1, R),
    domain([Height], 0, R),
    Length*Height #=< H,                            % total area of each slice must be at most H
    Xi + Length -1 #=< C,
    Yi + Length -1 #=< R,
    N1 is N+1,
    buildDomainVariables(N1, MaxSlices, R, C, H, Vars, AreaOccup),
    AreaOccupied #= AreaOccup + (Length*Height).


buildRectangles([], []).
buildRectangles([Xi, Length, Yi, Height | Vars], [f(Xi, Length, Yi, Height) | Rectangles]) :-
    buildRectangles(Vars, Rectangles).


minimumIngredients(_, _, _, _, _, []).
minimumIngredients(Pizza, R, C, L, H, [Xi, Length, Yi, Height | Vars]) :-
    getGrid(1, 1, R, C, Xi, Length, Yi, Height, Grid),
    scalar_product(Pizza, Grid, #=, Value),
    Min is L,
    Max is H-L,
    (
        (Length #= 0 #/\ Height #= 0)
        #\/
        (Length #\= 0 #/\ Height #\= 0 #/\ Value #>= Min #/\ Value #=< Max)
    ),
    minimumIngredients(Pizza, R, C, L, H, Vars).


getGrid(Line, _, R, _, _, _, _, _, []) :-
    Line =:= R+1.

getGrid(Line, Column, R, C, Xi, Length, Yi, Height, Grid) :-
    Column =:= C+1,
    Line1 is Line+1,
    getGrid(Line1, 1, R, C, Xi, Length, Yi, Height, Grid).

getGrid(Line, Column, R, C, Xi, Length, Yi, Height, [B | Grid]) :-
    (
        Line #>= Yi #/\ Line #< Yi+Height
        #/\
        Column #>= Xi #/\ Column #< Xi+Length
    ) #<=> B,
    Column1 is Column+1,
    getGrid(Line, Column1, R, C, Xi, Length, Yi, Height, Grid).


printSolution([]).
printSolution([Xi, Length, Yi, Height | Vars]) :-
    Xf is Xi + Length - 2,
    Yf is Yi + Height - 2,
    Xii is Xi -1,
    Yii is Yi -1,
    format('~w ~w ~w ~w~n', [Yii,  Xii, Yf, Xf]),
    printSolution(Vars).
