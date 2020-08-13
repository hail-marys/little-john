import little_john.add_to_target_list as LJ
import builtins

# Test in own file
# Test every functionality of program
# So do the builtins

# Replace print and input 


def mock_print(*args, **kwargs):
    return str(*args) + '\n'

builtins.print = mock_print

# Unit tests:

def test_sub_menu_exists():
    assert LJ.sub_menu


def test_add_compan_to_tageted_comapanies_exists():
    assert LJ.add_company_to_targeted_companies


def test_remove_company_from_targeted_companies_exists():
    assert LJ.remove_company_from_targeted_companies


def test_is_real_company_exists():
    assert LJ.is_real_company


def test_is_unique_exists():
    assert LJ.is_unique


def test_view_companies_exists():
    assert LJ.view_companies


def test_sub_menu_print():
    assert LJ.sub_menu() == """
Targeted Companies List
-----------------------

Would you like to:
1. View current companies
2. Add a company
3. Add all S&P 500 Index companies to list
4. Remove a company
5. Remove all companies
6. Go back to main menu
    
>
"""


