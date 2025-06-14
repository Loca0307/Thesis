// clientInvoicesDescriptions.ts

import { INodeProperties } from 'n8n-workflow';

// Descriptions for the "List client invoices" operation
export const listClientInvoicesDescription: INodeProperties[] = [
    {
        displayName: 'Organization ID',
        name: 'organizationId',
        type: 'string',
        default: '',
        required: true,
        description: 'The unique identifier of the organization whose client invoices are to be fetched.',
    },
    {
        displayName: 'Status',
        name: 'status',
        type: 'options',
        options: [
            { name: 'All', value: 'all' },
            { name: 'Pending', value: 'pending' },
            { name: 'Paid', value: 'paid' },
        ],
        default: 'all',
        required: false,
        description: 'Filter client invoices by their payment status.',
    },
    {
        displayName: 'Start Date',
        name: 'startDate',
        type: 'dateTime',
        default: '',
        required: false,
        description: 'Fetch invoices created after this date.',
    },
    {
        displayName: 'End Date',
        name: 'endDate',
        type: 'dateTime',
        default: '',
        required: false,
        description: 'Fetch invoices created before this date.',
    },
];

// Descriptions for the "Create a client invoice" operation
export const createClientInvoiceDescription: INodeProperties[] = [
    {
        displayName: 'Organization ID',
        name: 'organizationId',
        type: 'string',
        default: '',
        required: true,
        description: 'The unique identifier of the organization for which the client invoice will be created.',
    },
    {
        displayName: 'Client Invoice',
        name: 'clientInvoice',
        type: 'fixedCollection',
        typeOptions: {
            multipleValues: false,
        },
        default: {},
        required: true,
        description: 'Details of the client invoice to be created.',
        options: [
            {
                displayName: 'Invoice Details',
                name: 'invoiceDetails',
                values: [
                    {
                        displayName: 'Invoice Number',
                        name: 'invoiceNumber',
                        type: 'string',
                        default: '',
                        required: true,
                        description: 'Unique number of the client invoice.',
                    },
                    {
                        displayName: 'Invoice Date',
                        name: 'invoiceDate',
                        type: 'dateTime',
                        default: '',
                        required: true,
                        description: 'Date of the client invoice.',
                    },
                    {
                        displayName: 'Due Date',
                        name: 'dueDate',
                        type: 'dateTime',
                        default: '',
                        required: true,
                        description: 'Due date for the client invoice payment.',
                    },
                    {
                        displayName: 'Amount',
                        name: 'amount',
                        type: 'number',
                        default: '',
                        required: true,
                        description: 'Amount of the client invoice.',
                    },
                    {
                        displayName: 'Currency',
                        name: 'currency',
                        type: 'string',
                        default: 'EUR',
                        required: true,
                        description: 'Currency of the client invoice.',
                    },
                    {
                        displayName: 'Description',
                        name: 'description',
                        type: 'string',
                        default: '',
                        required: false,
                        description: 'Description or details of the client invoice.',
                    },
                ],
            },
        ],
    },
];