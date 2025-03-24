"""
Test case for the crewai_visualization.py CLI entry point
"""

import os
import sys
import unittest
from unittest.mock import patch, MagicMock
import tempfile
import shutil

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class TestVisualizationCLI(unittest.TestCase):
    """Test the CLI entry point for the visualization module"""
    
    def setUp(self):
        """Set up test environment"""
        # Create a temporary directory for test outputs
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_analysis.md")
        
        # Create a test analysis file
        test_content = """# Test Analysis Results
        
## Sales Metrics
- Total Sales: $5000
- Average Order Value: $100
- Average Items per Order: 3.5

## Customer Metrics
- Repeat Customers: 65%
- One-Time Customers: 35%

## Top 5 Selling Products by Quantity:
1. Product: MED123, Quantity: 500
2. Product: MED456, Quantity: 350
3. Product: MED789, Quantity: 220
4. Product: MED012, Quantity: 180
5. Product: MED345, Quantity: 150
"""
        with open(self.test_file, 'w') as f:
            f.write(test_content)
            
    def tearDown(self):
        """Clean up after tests"""
        # Remove temporary directory
        shutil.rmtree(self.test_dir)
        
    @patch('Core_Scripts.crewai_visualization.visualize_analysis_results')
    def test_cli_with_file_argument(self, mock_visualize):
        """Test the CLI with a file argument"""
        # Set up mock return value
        mock_visualize.return_value = {
            'top_products_chart': os.path.join(self.test_dir, 'chart.html'),
            'enhanced_markdown': os.path.join(self.test_dir, 'enhanced.md')
        }
        
        # Mock sys.argv
        test_args = ['crewai_visualization.py', '--file', self.test_file, '--output-dir', self.test_dir]
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "crewai_visualization.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                try:
                    # This will exit with SystemExit in actual execution
                    # but we catch it for testing
                    spec.loader.exec_module(main_module)
                except SystemExit:
                    pass
        
        # Verify visualize_analysis_results was called with correct arguments
        mock_visualize.assert_called_once_with(input_file=self.test_file, output_dir=self.test_dir)
        
    @patch('Core_Scripts.crewai_visualization.visualize_analysis_results')
    def test_cli_with_content_argument(self, mock_visualize):
        """Test the CLI with direct content"""
        # Set up mock return value
        mock_visualize.return_value = {
            'top_products_chart': os.path.join(self.test_dir, 'chart.html'),
            'enhanced_markdown': os.path.join(self.test_dir, 'enhanced.md')
        }
        
        test_content = "# Test Analysis\nSome test content"
        
        # Mock sys.argv
        test_args = ['crewai_visualization.py', '--content', test_content, '--output-dir', self.test_dir]
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "crewai_visualization.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                try:
                    # This will exit with SystemExit in actual execution
                    # but we catch it for testing
                    spec.loader.exec_module(main_module)
                except SystemExit:
                    pass
        
        # Verify visualize_analysis_results was called with correct arguments
        mock_visualize.assert_called_once_with(content=test_content, output_dir=self.test_dir)
        
    @patch('Core_Scripts.crewai_visualization.visualize_analysis_results')
    @patch('Core_Scripts.crewai_visualization.export_visualizations_as_zip')
    def test_cli_with_zip_option(self, mock_zip, mock_visualize):
        """Test the CLI with zip option"""
        # Set up mock return values
        mock_visualize.return_value = {
            'top_products_chart': os.path.join(self.test_dir, 'chart.html'),
            'enhanced_markdown': os.path.join(self.test_dir, 'enhanced.md')
        }
        mock_zip.return_value = os.path.join(self.test_dir, 'visuals_bundle.zip')
        
        # Mock sys.argv
        test_args = ['crewai_visualization.py', '--file', self.test_file, '--output-dir', self.test_dir, '--zip']
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "crewai_visualization.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                try:
                    # This will exit with SystemExit in actual execution
                    # but we catch it for testing
                    spec.loader.exec_module(main_module)
                except SystemExit:
                    pass
        
        # Verify both functions were called with correct arguments
        mock_visualize.assert_called_once_with(input_file=self.test_file, output_dir=self.test_dir)
        mock_zip.assert_called_once_with(self.test_dir)

if __name__ == '__main__':
    unittest.main()