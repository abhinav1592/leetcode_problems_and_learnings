
Array Problems from Leetcode
<br>
<br>


1.  <a href= "https://leetcode.com/problems/count-number-of-teams/">1395 -  Count Number of Teams</a> <br>
   <a href="https://github.com/abhinav1592/leetcode_problems_and_learnings/blob/master/Data%20Structures/Array/1395.py">Solution Link</a><br>
   <br>
	 Learnings:<br>
<ul>
	 <ol>  Read the inputs properly before coding up on paper/editor.</ol>
	 <ol>  Check for variables which remain undefined ( n vs len(given_parameter)). </ol>
	 <ol>  Check for usage of enumerate vs range in Python3.</ol>
	 <ol>  Initialize array with 0 elements - len(you_want_to_initialize)*[0]</ol>

   <ol>  Counting the number of elements greater or less than current element position is O(n^2)
	    and you can avoid extra space to maintain it.</ol>
	<ol>  Solution which is in the link uses extra-space and next time when you visit this
	    problem, try to solve with O(1) space.</ol>

</ul>
<br>
<br>
2.  1329 -  Sort the Matrix Diagonally <br>
	 Problem Link: https://leetcode.com/problems/sort-the-matrix-diagonally/ <br>
	 Solution Link: https://github.com/abhinav1592/leetcode_problems_and_learnings/blob/master/Data%20Structures/Array/1329.py<br>
	 Learnings:<br>
	 a.  A[i][j] on the same diagonal have same value of i - j.<br>
	 b.  Reverse sort - Array.sort(reverse=1)<br>
	 c.  Learn to use zip and iter through this solution: https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/489846/Several-Python-solutions and try solving
	 with less space.<br>



