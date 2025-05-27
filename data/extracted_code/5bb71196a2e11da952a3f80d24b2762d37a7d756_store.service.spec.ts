



// Some more tests for the StoreService
describe('StoreService', () => {
  let service: StoreService;
  let httpMock: HttpTestingController;

  const STORE_BASE_URL = 'http://localhost:8080/api/v1';

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [StoreService],
    });
    service = TestBed.inject(StoreService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should fetch API data with default parameters', () => {
    const keyword = '';
    const page = 0;
    const size = 10;
    const sort = 'asc';
    const expectedUrl = `${STORE_BASE_URL}/products?keyword=${keyword}&page=${page}&size=${size}&sort=${sort}`;
    const expectedResponse: ApiResponse<Page<Product[]>> = {
      data: {
        content: [],
        totalPages: 0,
        totalElements: 0,
        number: 0,
        size: 10,
        pageable: {
          sort: {
            empty: false,
            sorted: false,
            unsorted: false
          },
          offset: 0,
          pageNumber: 0,
          pageSize: 0,
          paged: false,
          unpaged: false
        },
        last: false,
        sort: {
          empty: false,
          sorted: false,
          unsorted: false
        },
        numberOfElements: 0,
        first: false,
        empty: false
      },
      timeStamp: '',
      statusCode: 0,
      status: '',
      message: ''
    };

    service.fetchApiData().subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('GET');
    req.flush(expectedResponse);
  });

  it('should fetch API data with custom parameters', () => {
    const keyword = 'test';
    const page = 1;
    const size = 12;
    const sort = 'name-asc';
    const expectedUrl = `${STORE_BASE_URL}/products?keyword=${keyword}&page=${page}&size=${size}&sort=${sort}`;
    const expectedResponse: ApiResponse<Page<Product[]>> = {
      data: {
        content: [],
        totalPages: 0,
        totalElements: 0,
        number: 0,
        size: 10,
        pageable: {
          sort: {
            empty: false,
            sorted: false,
            unsorted: false
          },
          offset: 0,
          pageNumber: 0,
          pageSize: 0,
          paged: false,
          unpaged: false
        },
        last: false,
        sort: {
          empty: false,
          sorted: false,
          unsorted: false
        },
        numberOfElements: 0,
        first: false,
        empty: false
      },
      timeStamp: '',
      statusCode: 0,
      status: '',
      message: ''
    };

    service.fetchApiData(keyword, page, size, sort).subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('GET');
    req.flush(expectedResponse);
  });

  it('should find product by id', () => {
    const productId = 1;
    const expectedUrl = `${STORE_BASE_URL}/products/${productId}`;
    const expectedResponse = { id: 1, name: 'Test Product', price: 9.99 };

    service.findProductById(productId).subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('GET');
    req.flush(expectedResponse);
  });

  it('should place order', () => {
    const order = { id: 1, name: 'Test Order', total: 9.99 };
    const expectedUrl = `${STORE_BASE_URL}/orders/new`;
    const expectedResponse: ApiResponse<any> = {
      data: order,
      timeStamp: '',
      statusCode: 0,
      status: '',
      message: ''
    };

    service.placeOrder(order).subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('POST');
    req.flush(expectedResponse);
  });

  it('should get orders for user', () => {
    const userId = '1';
    const expectedUrl = `${STORE_BASE_URL}/orders/user/${userId}`;
    const expectedResponse = [{ id: 1, name: 'Test Order', total: 9.99 }];

    service.getOrdersForUser(userId).subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('GET');
    req.flush(expectedResponse);
  });

  it('should get order by order id', () => {
    const orderId = '1';
    const expectedUrl = `${STORE_BASE_URL}/orders/id/${orderId}`;
    const expectedResponse = { id: 1, name: 'Test Order', total: 9.99 };

    service.getOrderById(orderId).subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('GET');
    req.flush(expectedResponse);
  });

  it('should get product by product id', () => {
    const productId = '1';
    const expectedUrl = `${STORE_BASE_URL}/products/${productId}`;
    const expectedResponse = { id: 1, name: 'Test Product', price: 9.99 };

    service.getProductByProductId(productId).subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('GET');
    req.flush(expectedResponse);
  });

  it('should update order status', () => {
    const orderId = '1';
    const status = 'SHIPPED';
    const expectedUrl = `${STORE_BASE_URL}/orders/${orderId}/status/${status}`;
    const expectedResponse = { id: 1, name: 'Test Order', total: 9.99, status: 'SHIPPED' };

    service.updateOrderStatus(orderId, status).subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('PUT');
    req.flush(expectedResponse);
  });

  it('should update order item status', () => {
    const orderNumber = '1';
    const orderItemId = '1';
    const status = 'SHIPPED';
    const expectedUrl = `${STORE_BASE_URL}/orders/${orderNumber}/orderItem/${orderItemId}/status/${status}`;
    const expectedResponse = { id: '1', name: 'Test Order Item', total: 9.99, status: 'SHIPPED' };

    service.updateOrderItemStatus(orderNumber, orderItemId, status).subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('PUT');
    req.flush(expectedResponse);
  });

  it('should get user by user id', () => {
    const userId = '1';
    const expectedUrl = `${STORE_BASE_URL}/user/${userId}`;
    const expectedResponse = { id: '1', name: 'Test User' };

    service.getUserByUserId(userId).subscribe((res) => {
      expect(res).toEqual(expectedResponse);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('GET');
    req.flush(expectedResponse);
  });

  it('should update user first name', () => {
    const userId = '1';
    const firstName = 'John';
    const expectedUrl = `${STORE_BASE_URL}/user/${userId}/first-name`;

    service.updateUserFirstName(userId, firstName).subscribe((res) => {
      expect(res).toEqual(firstName);
    });

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('PUT');
    expect(req.request.body).toBe(firstName);
    req.flush(firstName);
  });

  it('should update user last name', () => {
    const userId = '1';
    const lastName = 'Doe';
    const expectedUrl = `${STORE_BASE_URL}/user/${userId}/last-name`;

    service.updateUserLastName(userId, lastName).subscribe();

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('PUT');
    expect(req.request.body).toBe(lastName);
    req.flush(null);
  });

  it('should update user email', () => {
    const email = 'test@example.com';
    const newEmail = 'newtest@example.com';
    const expectedUrl = `${STORE_BASE_URL}/user/update-email?email=${email}&newEmail=${newEmail}`;

    service.updateUserEmail(email, newEmail).subscribe();

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('PUT');
    req.flush(null);
  });

  it('should update user phone number', () => {
    const userId = '1';
    const phone = '1234567890';
    const expectedUrl = `${STORE_BASE_URL}/user/${userId}/phone-number`;

    service.updateUserPhoneNumber(userId, phone).subscribe();

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('PUT');
    expect(req.request.body).toBe(phone);
    req.flush(null);
  });

  it('should update user address', () => {
    const userId = '1';
    const address = '123 Foo St';
    const expectedUrl = `${STORE_BASE_URL}/user/${userId}/address`;

    service.updateUserAddress(userId, address).subscribe();

    const req = httpMock.expectOne(expectedUrl);
    expect(req.request.method).toBe('PUT');
    expect(req.request.body).toBe(address);
    req.flush(null);
  });
});