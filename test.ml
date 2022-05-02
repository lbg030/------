(* HW 2 *)

type nat = O | S of nat 

(* Exercise 1 *)
let rec natadd n1 n2 = 
	match n1 with 
	| O -> n2 
	| S n1' -> S (natadd n1' n2)  

(* Exercise 1 *)
let rec natmul n1 n2 = 
	match n1 with 
	| O -> O 
	| S n1' -> natadd (natmul n1' n2) n2  

(* Exercise 2 *)
let rec is_even n = 
	match n with 
	| O -> true 
	| S n' -> not (is_even n') 

(* Exercise 2 *)
let rec leq n1 n2 = 
	match n1, n2 with 
	| O, _ -> true 
	| S n1', S n2' -> leq n1' n2'
	| _ -> false  

(* Exercise 3 *)
let rec is_squared n = 
	let rec f n' =
		if leq (S n) n' then false   
		else 
			if (natmul n' n') = n then true 
			else f (S n')
	in
	f O 
	
type nat_list = Nil | Cons of nat * nat_list 

(* Exercise 4 *)
let rec for_all f l = 
	match l with 
	| Nil -> true 
	| Cons (n, l') -> (f n) && (for_all f l') 

(* Exercise 5 *)
let rec filter_not f l = 
	match l with 
	| Nil -> Nil 
	| Cons (n, l') -> if f n then filter_not f l' else Cons (n, filter_not f l')  

type btree = Leaf | Node of int * btree * btree 

(* Exercise 6 *)
let rec count_leaves t = 
	match t with 
	| Leaf -> 1 
	| Node (_, l, r) -> 
		(count_leaves l) + (count_leaves r)

(* Exercise 7 *)
let rec double_tree t = 
	match t with 
	| Leaf -> Leaf 
	| Node (n, l, r) -> 
		Node (2*n, double_tree l, double_tree r) 

type direction = Left | Right 
and path = NoPath | Path of direction list 

(* Exercise 8 *)
let rec tree_path (t:btree) (n:int) : path = 
	match t with 
	| Leaf -> NoPath  
	| Node (n', l, r) -> 
		if n = n' then Path [] 
		else 
			let lpath = tree_path l n in
			match lpath with 
			| Path path -> Path (Left :: path) 
			| NoPath -> 
				let rpath = tree_path r n in 
				match rpath with 
				| Path path -> Path (Right :: path) 
				| NoPath -> NoPath 			  
	
