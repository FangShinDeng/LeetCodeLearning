WITH cte1 AS (
	SELECT 
		d.name as department_name,
        e.name as employee_name,
		e.score,
		RANK () OVER (
			partition by d.name 
			order by e.score DESC
		) score_rank
	FROM 
		employee e
			LEFT JOIN
		department d ON e.department_id = d.id ORDER BY d.id ASC
) select * from cte1 where cte1.score_rank < 3;