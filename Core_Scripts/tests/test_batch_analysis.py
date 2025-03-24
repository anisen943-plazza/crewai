"""
Test case for the batch_analysis.py CLI entry point and core functionality
"""

import os
import sys
import unittest
from unittest.mock import patch, MagicMock, mock_open
import tempfile
import shutil
from datetime import datetime, timedelta
import re

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class TestBatchAnalysisCLI(unittest.TestCase):
    """Test the CLI entry point and core functionality for batch_analysis.py"""
    
    def setUp(self):
        """Set up test environment"""
        # Create a temporary directory for test outputs
        self.test_dir = tempfile.mkdtemp()
        self.test_output_dir = os.path.join(self.test_dir, "output")
        os.makedirs(self.test_output_dir, exist_ok=True)
        
        # Create a test analysis file
        self.test_analysis_file = os.path.join(self.test_dir, "test_analysis.md")
        test_content = """# Test Analysis Results
        
## Full Analysis on 2025-03-23 12:00:00

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
        with open(self.test_analysis_file, 'w') as f:
            f.write(test_content)
            
    def tearDown(self):
        """Clean up after tests"""
        # Remove temporary directory
        shutil.rmtree(self.test_dir)
        
    @patch('Core_Scripts.batch_analysis.run_batch_analysis')
    def test_cli_basic_execution(self, mock_run_analysis):
        """Test the basic CLI execution without arguments"""
        # Set up mock return value
        mock_run_analysis.return_value = ("Analysis completed", self.test_output_dir)
        
        # Mock sys.argv
        test_args = ['batch_analysis.py']
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "batch_analysis.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                try:
                    # This will exit with SystemExit if args are invalid
                    spec.loader.exec_module(main_module)
                except SystemExit:
                    pass
        
        # Verify run_batch_analysis was called with default arguments
        mock_run_analysis.assert_called_once_with(
            force=False, 
            skip_visualization=False,
            output_dir=None,
            viz_only=False
        )
        
    @patch('Core_Scripts.batch_analysis.run_batch_analysis')
    def test_cli_with_force_flag(self, mock_run_analysis):
        """Test the CLI with --force flag"""
        # Set up mock return value
        mock_run_analysis.return_value = ("Analysis completed", self.test_output_dir)
        
        # Mock sys.argv
        test_args = ['batch_analysis.py', '--force']
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "batch_analysis.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                try:
                    spec.loader.exec_module(main_module)
                except SystemExit:
                    pass
        
        # Verify run_batch_analysis was called with force=True
        mock_run_analysis.assert_called_once_with(
            force=True, 
            skip_visualization=False,
            output_dir=None,
            viz_only=False
        )
        
    @patch('Core_Scripts.batch_analysis.run_batch_analysis')
    def test_cli_with_no_viz_flag(self, mock_run_analysis):
        """Test the CLI with --no-viz flag"""
        # Set up mock return value
        mock_run_analysis.return_value = ("Analysis completed", self.test_output_dir)
        
        # Mock sys.argv
        test_args = ['batch_analysis.py', '--no-viz']
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "batch_analysis.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                try:
                    spec.loader.exec_module(main_module)
                except SystemExit:
                    pass
        
        # Verify run_batch_analysis was called with skip_visualization=True
        mock_run_analysis.assert_called_once_with(
            force=False, 
            skip_visualization=True,
            output_dir=None,
            viz_only=False
        )
        
    @patch('Core_Scripts.batch_analysis.run_batch_analysis')
    def test_cli_with_output_dir(self, mock_run_analysis):
        """Test the CLI with --output-dir option"""
        # Set up mock return value
        mock_run_analysis.return_value = ("Analysis completed", self.test_output_dir)
        
        # Mock sys.argv
        test_args = ['batch_analysis.py', '--output-dir', self.test_output_dir]
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "batch_analysis.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                try:
                    spec.loader.exec_module(main_module)
                except SystemExit:
                    pass
        
        # Verify run_batch_analysis was called with custom output_dir
        mock_run_analysis.assert_called_once_with(
            force=False, 
            skip_visualization=False,
            output_dir=self.test_output_dir,
            viz_only=False
        )
        
    @patch('Core_Scripts.batch_analysis.run_batch_analysis')
    def test_cli_with_viz_only_flag(self, mock_run_analysis):
        """Test the CLI with --viz-only flag"""
        # Set up mock return value
        mock_run_analysis.return_value = ("Visualization completed", self.test_output_dir)
        
        # Mock sys.argv
        test_args = ['batch_analysis.py', '--viz-only']
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "batch_analysis.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                try:
                    spec.loader.exec_module(main_module)
                except SystemExit:
                    pass
        
        # Verify run_batch_analysis was called with viz_only=True
        mock_run_analysis.assert_called_once_with(
            force=False, 
            skip_visualization=False,
            output_dir=None,
            viz_only=True
        )
        
    @patch('Core_Scripts.batch_analysis.run_batch_analysis')
    def test_cli_conflicting_flags(self, mock_run_analysis):
        """Test the CLI with conflicting flags (--no-viz and --viz-only)"""
        # Set up mock return value
        mock_run_analysis.return_value = ("Analysis completed", self.test_output_dir)
        
        # Mock sys.argv - these flags are conflicting and should trigger an error
        test_args = ['batch_analysis.py', '--no-viz', '--viz-only']
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "batch_analysis.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                # Should exit with sys.exit(1)
                with self.assertRaises(SystemExit) as cm:
                    spec.loader.exec_module(main_module)
                self.assertEqual(cm.exception.code, 1)  # Check exit code is 1
        
        # Verify run_batch_analysis was NOT called due to validation error
        mock_run_analysis.assert_not_called()
        
    @patch('Core_Scripts.batch_analysis.run_batch_analysis')
    def test_cli_force_with_viz_only(self, mock_run_analysis):
        """Test the CLI with --force and --viz-only together (force should be ignored)"""
        # Set up mock return value
        mock_run_analysis.return_value = ("Visualization completed", self.test_output_dir)
        
        # Mock sys.argv
        test_args = ['batch_analysis.py', '--force', '--viz-only']
        with patch('sys.argv', test_args):
            # Import __main__ function and run it
            import importlib.util
            spec = importlib.util.spec_from_file_location("__main__", 
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                "batch_analysis.py"))
            main_module = importlib.util.module_from_spec(spec)
            
            # Mock print to prevent output during tests
            with patch('builtins.print'):
                spec.loader.exec_module(main_module)
        
        # Verify run_batch_analysis was called with force=False (--force ignored)
        mock_run_analysis.assert_called_once_with(
            force=False,  # --force should be ignored
            skip_visualization=False,
            output_dir=None,
            viz_only=True  # --viz-only
        )
    
    @patch('os.path.exists')
    @patch('os.path.getmtime')
    @patch('builtins.open', new_callable=mock_open)
    @patch('datetime.datetime', wraps=datetime)
    def test_check_kb_freshness_with_recent_timestamp(self, mock_datetime, mock_file, mock_getmtime, mock_exists):
        """Test check_kb_freshness when KB has a recent timestamp in content"""
        from Core_Scripts.batch_analysis import check_kb_freshness
        
        # Mock datetime.now() to return a fixed current time
        current_time = datetime(2025, 3, 24, 12, 0, 0)
        mock_datetime.now.return_value = current_time
        
        # Mock file modification time (1 day old)
        mock_getmtime.return_value = (current_time - timedelta(days=1)).timestamp()
        
        # Mock file existence
        mock_exists.return_value = True
        
        # Mock file content with timestamp (5 hours old)
        recent_timestamp = (current_time - timedelta(hours=5)).strftime('%Y-%m-%d %H:%M:%S')
        mock_file.return_value.read.return_value = f"## Full Analysis on {recent_timestamp}"
        
        # Call the function
        is_fresh, last_updated = check_kb_freshness(max_age_days=7)
        
        # Assertions
        self.assertTrue(is_fresh)  # KB should be considered fresh (5 hours old)
        self.assertEqual(last_updated, current_time - timedelta(hours=5))
    
    @patch('os.path.exists')
    @patch('os.path.getmtime')
    @patch('builtins.open', new_callable=mock_open)
    @patch('datetime.datetime', wraps=datetime)
    def test_check_kb_freshness_with_old_timestamp(self, mock_datetime, mock_file, mock_getmtime, mock_exists):
        """Test check_kb_freshness when KB has an old timestamp in content"""
        from Core_Scripts.batch_analysis import check_kb_freshness
        
        # Mock datetime.now() to return a fixed current time
        current_time = datetime(2025, 3, 24, 12, 0, 0)
        mock_datetime.now.return_value = current_time
        
        # Mock file modification time (10 days old)
        mock_getmtime.return_value = (current_time - timedelta(days=10)).timestamp()
        
        # Mock file existence
        mock_exists.return_value = True
        
        # Mock file content with timestamp (8 days old)
        old_timestamp = (current_time - timedelta(days=8)).strftime('%Y-%m-%d %H:%M:%S')
        mock_file.return_value.read.return_value = f"## Full Analysis on {old_timestamp}"
        
        # Call the function
        is_fresh, last_updated = check_kb_freshness(max_age_days=7)
        
        # Assertions
        self.assertFalse(is_fresh)  # KB should be considered stale (8 days old)
        self.assertEqual(last_updated, current_time - timedelta(days=8))
    
    @patch('os.path.exists')
    def test_check_kb_freshness_no_file(self, mock_exists):
        """Test check_kb_freshness when knowledge file doesn't exist"""
        from Core_Scripts.batch_analysis import check_kb_freshness
        
        # Mock file nonexistence
        mock_exists.return_value = False
        
        # Call the function
        is_fresh, last_updated = check_kb_freshness(max_age_days=7)
        
        # Assertions
        self.assertFalse(is_fresh)  # KB should be considered non-existent
        self.assertIsNone(last_updated)
    
    @patch('os.path.exists')
    @patch('Core_Scripts.batch_analysis.glob')
    @patch('os.path.getmtime')
    def test_get_latest_analysis_file(self, mock_getmtime, mock_glob, mock_exists):
        """Test get_latest_analysis_file finds the most recent file"""
        from Core_Scripts.batch_analysis import get_latest_analysis_file
        
        # Mock file existence
        mock_exists.side_effect = lambda path: 'knowledge' in path  # Only the knowledge path exists
        
        # Mock glob results
        mock_glob.return_value = []  # No glob matches
        
        # Mock modification times (newer for knowledge file)
        knowledge_path = os.path.join('knowledge', 'sales_analysis_results.md')
        mock_getmtime.side_effect = lambda path: 1616600000 if 'knowledge' in path else 1616500000
        
        # Call the function
        result = get_latest_analysis_file()
        
        # The result should contain the knowledge path since it's the only one that exists
        self.assertIsNotNone(result)
        self.assertTrue('knowledge' in result)
    
    @patch('Core_Scripts.plazza_analytics.run_analysis')
    @patch('Core_Scripts.batch_analysis.check_kb_freshness')
    @patch('crewai_visualization.visualize_analysis_results')
    @patch('crewai_visualization.export_visualizations_as_zip')
    def test_run_batch_analysis_full_flow(self, mock_zip, mock_visualize, mock_check_freshness, mock_run_analysis):
        """Test run_batch_analysis with the full flow (fresh analysis + visualization)"""
        from Core_Scripts.batch_analysis import run_batch_analysis
        
        # Mock return values
        mock_check_freshness.return_value = (False, None)  # Not fresh, need to run analysis
        mock_run_analysis.return_value = "Analysis result"
        mock_visualize.return_value = {"chart": "chart.html"}
        mock_zip.return_value = "visuals_bundle.zip"
        
        # Call the function
        result, output_dir = run_batch_analysis(force=False, skip_visualization=False)
        
        # Assertions
        mock_check_freshness.assert_called_once()
        mock_run_analysis.assert_called_once()
        mock_visualize.assert_called_once()
        mock_zip.assert_called_once()
        self.assertEqual(result, "Analysis result")
    
    @patch('Core_Scripts.batch_analysis.check_kb_freshness')
    @patch('crewai_visualization.visualize_analysis_results')
    @patch('crewai_visualization.export_visualizations_as_zip')
    def test_run_batch_analysis_skip_fresh_kb(self, mock_zip, mock_visualize, mock_check_freshness):
        """Test run_batch_analysis skips analysis when KB is fresh"""
        from Core_Scripts.batch_analysis import run_batch_analysis
        
        # Mock return values
        mock_check_freshness.return_value = (True, datetime.now())  # KB is fresh
        mock_visualize.return_value = {"chart": "chart.html"}
        mock_zip.return_value = "visuals_bundle.zip"
        
        # Call the function with default values
        result, output_dir = run_batch_analysis()
        
        # Assertions
        mock_check_freshness.assert_called_once()
        self.assertTrue(result.startswith("Skipped analysis"))
        mock_visualize.assert_called_once()  # Should still generate visualizations
        mock_zip.assert_called_once()
    
    @patch('Core_Scripts.batch_analysis.check_kb_freshness')
    @patch('crewai_visualization.visualize_analysis_results')
    def test_run_batch_analysis_skip_visualization(self, mock_visualize, mock_check_freshness):
        """Test run_batch_analysis with skip_visualization=True"""
        from Core_Scripts.batch_analysis import run_batch_analysis
        
        # Mock return values
        mock_check_freshness.return_value = (True, datetime.now())  # KB is fresh
        
        # Call the function with skip_visualization=True
        result, output_dir = run_batch_analysis(skip_visualization=True)
        
        # Assertions
        mock_check_freshness.assert_called_once()
        mock_visualize.assert_not_called()  # Visualization should be skipped
    
    @patch('Core_Scripts.batch_analysis.get_latest_analysis_file')
    @patch('crewai_visualization.visualize_analysis_results')
    @patch('crewai_visualization.export_visualizations_as_zip')
    def test_run_batch_analysis_viz_only(self, mock_zip, mock_visualize, mock_get_analysis):
        """Test run_batch_analysis with viz_only=True"""
        from Core_Scripts.batch_analysis import run_batch_analysis
        
        # Mock return values
        mock_get_analysis.return_value = "/path/to/analysis.md"
        mock_visualize.return_value = {"chart": "chart.html"}
        mock_zip.return_value = "visuals_bundle.zip"
        
        # Call the function with viz_only=True
        result, output_dir = run_batch_analysis(viz_only=True)
        
        # Assertions
        mock_get_analysis.assert_called_once()
        mock_visualize.assert_called_once_with(input_file="/path/to/analysis.md", output_dir=output_dir)
        mock_zip.assert_called_once()
        self.assertTrue(result.startswith("Visualizations refreshed"))

if __name__ == '__main__':
    unittest.main()