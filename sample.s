(define square (lambda (x)
    (* x x)))

(define if (macro (predicate e1 e2)
	(cond (predicate e1)
		  (else e2))))

(define delay (macro (f)
	(lambda () f)))

(define force (lambda (p)
	(p)))
