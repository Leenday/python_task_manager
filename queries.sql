-- Показать работников у которых нет почты или почта не в корпоративном домене (домен dualbootpartners.com):
SELECT * FROM employees WHERE (email NOT LIKE '%dualbootpartners.com' OR email = NULL);

--Получить список работников нанятых в последние 30 дней:
SELECT * FROM employees WHERE hire_date > NOW() - INTERVAL '30 DAY';

--Найти максимальную и минимальную зарплату по каждому департаменту:
SELECT d.name, MAX(e.salary), MIN(e.salary) FROM departments d JOIN employees e ON e.department_id = d.id GROUP BY d.name;

--Посчитать количество работников в каждом регионе:
SELECT r.name, COUNT(e) FROM regions r JOIN departments d ON r.id = d.location_id JOIN employees e ON e.department_id = d.id GROUP BY r.id;

--Показать сотрудников у которых фамилия длиннее 10 символов:
SELECT name, last_name FROM employees WHERE LENGTH(last_name) > 10;

--Показать сотрудников с зарплатой выше средней по всей компании:
SELECT name, last_name FROM employees WHERE salary > (SELECT AVG(salary) from employees);

--Запросы на создание таблиц:
CREATE TABLE employees (id serial primary key, name varchar, last_name varchar, hire_date date, salary integer, email varchar, manager_id integer, department_id integer);

CREATE TABLE departments (id serial primary key, name varchar, location_id integer, manager_id integer);

CREATE TABLE locations (id serial primary key, address varchar, region_id integer);

CREATE TABLE regions (id serial primary key, name varchar);
