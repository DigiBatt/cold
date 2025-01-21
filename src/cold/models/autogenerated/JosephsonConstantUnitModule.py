
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class JosephsonConstantUnit(SIDimensionalUnit):
    """
    Class representing the `JosephsonConstantUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6b8bf0c9_4ec7_452c_bee5_26e5149a4f05'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'JosephsonConstantUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = JosephsonConstantUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_6b8bf0c9_4ec7_452c_bee5_26e5149a4f05',
    
    class_name='JosephsonConstantUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6b8bf0c9_4ec7_452c_bee5_26e5149a4f05',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'JosephsonConstantUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    