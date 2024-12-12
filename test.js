import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

// Define a custom metric to track failed requests
const failRate = new Rate('failed_requests');

export let options = {
    vus: 500, // Number of virtual users
    duration: '30s', // Test duration
    thresholds: {
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'http_req_failed': ['rate<0.01'], // Fail if more than 1% of requests fail
    },
};

export default function () {
    // Make an HTTPS request to the target URL
    let res = http.get('https://test.k6.io');
    
    // Check if the request was successful
    check(res, {
        'status is 200': (r) => r.status === 200,
        'transaction time OK': (r) => r.timings.duration < 500,
    });

    // Record failed requests
    failRate.add(res.status !== 200);

    // Simulate a think time between requests
    sleep(1);
}