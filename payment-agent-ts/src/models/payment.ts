export interface Payment {
    payment_id: string;
    gateway_status: string;
    amount: number;
    currency: string;
}

// export interface ApiResponse<T> {
//     data: T;
//     message: string;
// }