import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import { ProductsList } from "./productsList.jsx";
import { Link } from "react-router-dom";

export const AdminDashboard = () => {
    const {store, actions} = useContext(Context)

    useEffect(() => {
        actions.getProducts();
    }, []);


    return (



        <>
        <div className="container d-flex justify-text-center">
            <h2>Dashboard</h2>
        </div>
        <div className="container">
            <div className="row">
                <div className=" card p-1 col-lg-3 col-md-6 col-sm-12 col-xsm-12">
                    <h4 className="card-header">Tasks</h4>
                </div>
                <div className="card  col-lg-3 col-md-6 col-sm-12 col-xsm-12">
                    <div className="card-header row p-1 mb-2">
                        <h4 className="col-lg-8 col-md-8 col-sm-12">Products</h4>
                        <span className="col-lg-4 col-md-4 col-sm-12 float-right"><i className="fa-solid fa-plus "></i></span>
                        </div>
                   <ProductsList/>
                </div>
                <div className="card p-1 col-lg-3 col-md-6 col-sm-12 col-xsm-12">
                    <h4 className="card-header">Ingredients</h4>
                </div>
                <div className="card p-1 col-lg-3 col-md-6 col-sm-12 col-xsm-12">
                    <h4 className="card-header">Suppliers</h4>
                </div>            
            </div>
        </div>
        
        </>
        
    )
}