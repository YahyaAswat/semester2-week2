.mode table
.headers on

-- SHOW ALL LOANS
-- 1. Show book title, member name, and loan date.
-- SELECT Books.title, Members.name, Loans.loan_date 
-- FROM Loans 
-- JOIN Books on Books.id=Loans.book_id 
-- JOIN Members on Members.id=Loans.member_id


-- SHOW ALL BOOKS AND LOANS
-- 2. List all books and any loans associated with them.
-- SELECT Books.title, Members.name, Loans.loan_date 
-- FROM Books
-- LEFT JOIN Loans ON Books.id = Loans.book_id
-- LEFT JOIN Members ON Members.id = Loans.member_id;


-- SHOW ALL BRANCHES AND BOOKS  
-- 3. List all library branches and the books they hold.
-- SELECT LibraryBranch.name, Books.title
-- FROM LibraryBranch
-- LEFT JOIN Books on LibraryBranch.id=Books.branch_id

-- BRANCH AND BOOK COUNTS  
-- 4. Show each library branch and the number of books it holds.
-- SELECT LibraryBranch.name, COUNT(Books.id)
-- FROM LibraryBranch
-- LEFT JOIN Books on LibraryBranch.id=Books.branch_id 
-- GROUP BY LibraryBranch.id

  
-- 5. Show branches that hold more than 6 books.
-- SELECT LibraryBranch.name, COUNT(Books.id) as BookCount
-- FROM LibraryBranch
-- LEFT JOIN Books on LibraryBranch.id=Books.branch_id
-- GROUP BY LibraryBranch.id
-- HAVING BookCount>6

-- 10. **Books and loans report**  
-- Show all books and all loans, including books that were never loaned. 
-- Include a column classifying each row as “Loaned book” or “Unloaned book.”.
-- You will need to look up how to do this (hint: a case statement would work).

SELECT Books.name, Loans.loan_date
FROM Books
LEFT JOIN Loans on Books.id=Loans.book_id