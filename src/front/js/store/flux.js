const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			// Admin
			adminEmail: null,
			adminName: "",
			adminDepartment: null,
			adminIsLogedIn: false,
			// Login and users
			users: [],
			accessToken: null,
			isLogedIn: false,
			userEmail: "",
			userData: localStorage.getItem('user') ? localStorage.getItem('user') : '',
			// products
			products: [],
			allergies: [],
			currentAllergy: [],
			ingredients: [],
			suppliers: [],
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			]
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			getMessage: async () => {
				try{
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				}catch(error){
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			},

			loginAdmin: async (dataToSend) => {
				const uri = `${process.env.BACKEND_URL}/api/adminlogin`
				const options = {
					method: 'POST',
					headers: {
						'Content-type': 'application/json',
					},
					body: JSON.stringify(dataToSend)
				}
				const response = await fetch(uri, options)
				if (!response.ok) {
					console.log('Error: ', response.status, response.statusText);
					return
				}
				const data = await response.json();
				const access_token = data.access_token;
				setStore({ accessToken: access_token })
				setStore({ adminEmail: data.email })
				setStore({ adminName:  data.name})
				setStore({ adminDepartment: data.department })
				setStore({ adminIsLogedIn: true })
				localStorage.setItem('token', data.access_token)
				localStorage.setItem('admin', JSON.stringify(data.data))
			},

			addProducts: async (dataToSend) => {
				const url = `${process.env.BACKEND_URL}/api/admin/products`;
				const options = {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
						'Authorization': `Bearer ${getStore().accessToken}`
					},
					body: JSON.stringify(dataToSend),
				};

				const response = await fetch(url, options);
				if (!response.ok) {
					console.log("Error");
					return;
				}
				const newProduct = await response.json();
				setStore({ products: [...getStore().products, newProduct], newProductId: newProduct.id });
				
				console.log(newProduct);
			},

			getProducts: async () => {
				const url = `${process.env.BACKEND_URL}/api/products`;
				const options = {
					method: 'GET',
					headers: {
						'Content-Type': 'application/json'
					}
				}

				const response = await fetch(url, options)
				if (!response.ok) {
					console.log('Error: ', response.status, response.statusText);
					return
				}
				const data = await response.json()
				setStore({ products: data.results });
			
			},

			getAllergies: async () => {
				const url = `${process.env.BACKEND_URL}/api/allergies`;
				const options = {
					method: 'GET',
					headers: {
						'Content-Type': 'application/json'
					}
				}

				const response = await fetch(url, options)
				if (!response.ok) {
					console.log('Error: ', response.status, response.statusText);
					return
				}
				const data = await response.json()
				setStore({ allergies: data.results });
			
			},

			addAllergies: async (dataToSend) => {
				const url = `${process.env.BACKEND_URL}/api/admin/allergies`;
				const options = {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
						'Authorization': `Bearer ${getStore().accessToken}`
					},
					body: JSON.stringify(dataToSend),
				};

				const response = await fetch(url, options);
				if (!response.ok) {
					console.log("Error");
					return;
				}
				const newAllergy = await response.json();
				setStore({ allergies: [...getStore().allergies, newAllergy], newAllergyId: newAllergy.id });
				
				console.log(newAllergy);
			},

			editAllergies: async (dataToEdit, allergy_id) => {
				const url = `${process.env.BACKEND_URL}/api/admin/allergies/${allergy_id}`;
				const options = {
					method: "PUT",
					body: JSON.stringify(dataToEdit),
					headers: {
						'Content-Type': 'application/json',
						'Authorization':  `Bearer ${getStore().accessToken}`
					}
				};
				
				try {
					const response = await fetch(url, options);
					if (!response.ok) {
						console.log("Error updating allergy", response.status, response.statusText);
						return;
					}
					const updatedAllergy = await response.json();
					console.log("Updated Allergy:", updatedAllergy);
			
					// Update the allergies array with the edited allergy
					const updatedAllergies = getStore().allergies.map(allergy =>
						allergy.id === updatedAllergy.results.id ? updatedAllergy.results : allergy
					);
			
					setStore({ allergies: updatedAllergies });
					console.log("Allergy updated successfully");
				} catch (error) {
					console.error("Network or other error:", error);
				}
			},

			deleteAllergy: async 

			getIngredients: async () => {
				const url = `${process.env.BACKEND_URL}/api/ingredients`;
				const options = {
					method: 'GET',
					headers: {
						'Content-Type': 'application/json'
					}
				}

				const response = await fetch(url, options)
				if (!response.ok) {
					console.log('Error: ', response.status, response.statusText);
					return
				}
				const data = await response.json()
				setStore({ ingredients: data.results });
			
			},

		}
	};
};

export default getState;
