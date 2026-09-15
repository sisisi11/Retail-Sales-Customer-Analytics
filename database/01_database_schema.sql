-- Main customer table
CREATE DATABASE RetailAnalytics;
GO

USE RetailAnalytics;
GO


CREATE TABLE Customers
(
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100),
    City NVARCHAR(50),
    Country NVARCHAR(50),
    RegistrationDate DATE NOT NULL
);
GO


CREATE TABLE Products
(
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(100) NOT NULL,
    Category NVARCHAR(50) NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    
    CHECK (UnitPrice >= 0)
);
GO


CREATE TABLE Stores
(
    StoreID INT IDENTITY(1,1) PRIMARY KEY,
    StoreName NVARCHAR(100) NOT NULL,
    City NVARCHAR(50) NOT NULL,
    Country NVARCHAR(50) NOT NULL
);
GO


CREATE TABLE Promotions
(
    PromotionID INT IDENTITY(1,1) PRIMARY KEY,
    PromotionName NVARCHAR(100) NOT NULL,
    DiscountPercent DECIMAL(5,2) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,

    CHECK (DiscountPercent >= 0 AND DiscountPercent <= 100),
    CHECK (StartDate <= EndDate)
);
GO


CREATE TABLE Sales  -- Sales can come from a physical store or the online channel
                    -- StoreID is nullable because online sales may not be linked to a store
(
    SaleID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT NOT NULL,
    StoreID INT NULL,  /* In case if the purchase is online */
    SaleDate DATETIME2 NOT NULL,

    SalesChannel NVARCHAR(20) NOT NULL
    CONSTRAINT CK_Sales_SalesChannel --in case if we want to add mobile or other Channel..

    CHECK (SalesChannel IN ('Store', 'Online')), -- Keeps channel values consistent
    PromotionID INT NULL,

    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID),

    FOREIGN KEY (StoreID)
        REFERENCES Stores(StoreID),

    FOREIGN KEY (PromotionID)
        REFERENCES Promotions(PromotionID),
        
);
GO


CREATE TABLE SaleItems   --relation structure between Sales and SalesItems , we can have 1 order(sale) but with multiples items(SaleItems)
(
    SaleItemID INT IDENTITY(1,1) PRIMARY KEY,
    SaleID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (SaleID)
        REFERENCES Sales(SaleID),

    FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID),

    CHECK (Quantity > 0),
    CHECK (UnitPrice >= 0)
);
GO


CREATE TABLE Returns
(
    ReturnID INT IDENTITY(1,1) PRIMARY KEY,
    SaleItemID INT NOT NULL,
    ReturnDate DATE NOT NULL,
    ReturnQuantity INT NOT NULL,
    ReturnReason NVARCHAR(100),

    FOREIGN KEY (SaleItemID)
        REFERENCES SaleItems(SaleItemID),

    CHECK (ReturnQuantity > 0)
);
GO