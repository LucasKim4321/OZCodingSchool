use sakila;
select * from actor;

select first_name, count(*) as name_count from actor where actor_id < 100
group by first_name having first_name = 'penelope';