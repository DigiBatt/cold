
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .UnitSymbolModule import UnitSymbol







class BaseUnit(UnitSymbol):
    """
    Class representing the `BaseUnit` entity, which inherits from:
    - UnitSymbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_db716151_6b73_45ff_910c_d182fdcbb4f5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BaseUnit'`
        - **Alias**: `class_name`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BaseUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_db716151_6b73_45ff_910c_d182fdcbb4f5',
    
    class_name='BaseUnit',
    
    VIMTerm="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_db716151_6b73_45ff_910c_d182fdcbb4f5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BaseUnit',
        alias="class_name"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    