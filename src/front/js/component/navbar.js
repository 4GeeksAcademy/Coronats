import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

export const Navbar = () => {

	const {store, actions} = useContext(Context);

	return (
		<nav className="navbar navbar-light bg-light">
	{store.adminIsLogedIn ? 
	
				<>
				<Link to="/admin/dashboard">
					<span className="navbar-brand mb-0 h1">Hola {store.adminName}</span>
				</Link>
				<div className="ml-auto">
					<Link to="/admin/allergies">
						<button className="btn btn-primary">Allergies</button>
					</Link>
				</div>
				</>
				:
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
					<Link to="/admin/login">
						<button className="btn btn-primary">Check the Context in action</button>
					</Link>
				</div>
			</div>
			}
		</nav>
	);
};
