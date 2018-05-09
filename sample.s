(define square (lambda (x)
    (* x x)))

(define if (macro (predicate e1 e2)
	(cond (predicate e1)
		  (else e2))))

(define delay (macro (f)
	(lambda () f)))

(define force (lambda (p)
	(p)))

(define empty? (lambda (l)
	(= l ())))

(define map (lambda (f l)
	(cond ((empty? l) ())
		  (else (pair (f (head l))
		  	          (map f
		  	          	   (tail l)))))))
