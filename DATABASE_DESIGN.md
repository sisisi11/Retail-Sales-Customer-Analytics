# Initial Database Design

## Customers
- CustomerID
- FirstName
- LastName
- Email
- City
- Country
- RegistrationDate

## Products
- ProductID
- ProductName
- Category
- UnitPrice

## Stores
- StoreID
- StoreName
- City
- Country

## Sales
- SaleID
- CustomerID
- StoreID
- SaleDate
- SalesChannel
- PromotionID

## SaleItems
- SaleItemID
- SaleID
- ProductID
- Quantity
- UnitPrice

## Promotions
- PromotionID
- PromotionName
- DiscountPercent
- StartDate
- EndDate

## Returns
- ReturnID
- SaleItemID
- ReturnDate
- ReturnReason
