import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/lists.css";

export const ProductsList = () => {

const {store, actions} = useContext(Context)


    return (
        <ul className="list-group overflow-auto">
            {store.products.map((item, index) => (
                <li key={index} className="list-group-item mb-4 card">
                   <div className="row pl-0 ">
                        <div className="col-lg-4 col-md-3 col-sm-12 m-0">
                            <img src={item.image_url_1} alt={item.name} />    
                        </div>
                        <div className="col-lg-8 col-md-9 col-sm-12">
                            <h6>{item.name}</h6>  
                            <p>{item.price}€</p>
                        </div>
                    
                    </div>
                </li>
            )
            )}
        </ul>
    )
}