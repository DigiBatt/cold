
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalConstantModule import PhysicalConstant







class ExactConstant(PhysicalConstant):
    """
    Class representing the `ExactConstant` entity, which inherits from:
    - PhysicalConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_89762966_8076_4f7c_b745_f718d653e8e2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ExactConstant'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ExactConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_89762966_8076_4f7c_b745_f718d653e8e2',
    
    class_name='ExactConstant',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_89762966_8076_4f7c_b745_f718d653e8e2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ExactConstant',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    