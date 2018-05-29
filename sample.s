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
                (enum 1 (+ n 1) 1))))

(define prime? (lambda (y)
        (= (factors y)
           (pair 1 (pair y ())))))

(define primes_< (lambda (z)
        (filter prime? (enum 2 z 1))))

(define sum_primes_< (lambda (n)
        (reduce + 0 (primes_< n))))

(define loop (macro (n f)
        ((define _loop (lambda (i t)
                 (cond ((= i n) True)
                       (else (_loop (+ i 1) f)))))
         0
         0)))

(define begin (macro (l)
        ((define _begin (lambda (r t)
                 (cond ((empty? r) t)
                       (else (_begin (tail r)
                                     (eval (head r)))))))
          (quote l)
          ())))

(define f (macro l)
        ((lambda (n) (* n n))
         ($eval (+ l 1))))
