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

(define reduce (lambda (f i l)
        (cond ((empty? l) i)
              (else (f (head l)
                       (reduce f i (tail l)))))))

(define filter (lambda (p l)
        (cond ((empty? l) ())
              (else (cond ((p (head l)) 
                           (pair (head l)
                                 (filter p (tail l))))
                          (else (filter p (tail l))))))))

(define enum (lambda (a b d)
        (cond ((= a b) ())
              (else (pair a
                          (enum (+ a d)
                                b
                                d))))))

(define factors (lambda (n)
        (filter (lambda (x)
                    (= (mod n x) 0))
                (enum 2 n 1))))

(define prime (lambda (y)
        (= (factors y) ())))

(define primes_< (lambda (y)
        (filter prime (enum 2 y 1))))

(define sum_primes< (lambda (n)
        (reduce + 0 (primes_< n))))

