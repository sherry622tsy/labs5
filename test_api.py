import unittest
import json
from app import app

class UserApiTestCase(unittest.TestCase):

    def setUp(self):
        # 创建 Flask 测试客户端
        self.client = app.test_client()
        self.base_url = '/users'

        # 测试用户数据
        self.sample_user = {
            'name': 'Test User',
            'email': 'test@example.com',
            'height_cm': 170,
            'weight_kg': 65.5
        }

    def test_1_create_user(self):
        response = self.client.post(
            self.base_url,
            data=json.dumps(self.sample_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertIn('user_id', data)

        # 保存 user_id 供后续使用
        self.__class__.user_id = data['user_id']

    def test_2_get_all_users(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertIsInstance(data['users'], list)

    def test_3_get_single_user(self):
        response = self.client.get(f"{self.base_url}/{self.__class__.user_id}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['id'], self.__class__.user_id)

    def test_4_update_user(self):
        updated_data = {
            'name': 'Updated User',
            'email': 'updated@example.com',
            'height_cm': 172,
            'weight_kg': 66.0
        }
        response = self.client.put(
            f"{self.base_url}/{self.__class__.user_id}",
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])

    def test_5_delete_user(self):
        response = self.client.delete(f"{self.base_url}/{self.__class__.user_id}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])

        # 确认已删除
        follow_up = self.client.get(f"{self.base_url}/{self.__class__.user_id}")
        self.assertEqual(follow_up.status_code, 404)

if __name__ == '__main__':
    unittest.main()
