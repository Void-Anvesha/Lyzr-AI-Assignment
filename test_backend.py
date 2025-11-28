import unittest
from github_client import parse_pr_url
from diff_parser import parse_diff

class TestBackend(unittest.TestCase):
    def test_parse_pr_url(self):
        url = "https://github.com/owner/repo/pull/123"
        owner, repo, number = parse_pr_url(url)
        self.assertEqual(owner, "owner")
        self.assertEqual(repo, "repo")
        self.assertEqual(number, 123)
        
        url_invalid = "https://github.com/owner/repo"
        owner, repo, number = parse_pr_url(url_invalid)
        self.assertIsNone(owner)

    def test_diff_parser(self):
        diff_text = """diff --git a/file1.py b/file1.py
index 123..456 100644
--- a/file1.py
+++ b/file1.py
@@ -1,2 +1,2 @@
-print("Hello")
+print("Hello World")
diff --git a/file2.py b/file2.py
new file mode 100644
index 000..789
--- /dev/null
+++ b/file2.py
@@ -0,0 +1 @@
+def foo(): pass
"""
        files = parse_diff(diff_text)
        self.assertEqual(len(files), 2)
        self.assertEqual(files[0]['filename'], 'file1.py')
        self.assertIn('+print("Hello World")', files[0]['patch'])
        self.assertEqual(files[1]['filename'], 'file2.py')

if __name__ == '__main__':
    unittest.main()
