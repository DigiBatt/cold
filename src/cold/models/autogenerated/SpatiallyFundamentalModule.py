
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalModule import Fundamental







class SpatiallyFundamental(Fundamental):
    """
    Class representing the `SpatiallyFundamental` entity, which inherits from:
    - Fundamental

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f055e217_0b1b_4e7e_b8be_7340211b0c5e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpatiallyFundamental'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SpatiallyFundamental(
    
    class_iri='https://w3id.org/emmo#EMMO_f055e217_0b1b_4e7e_b8be_7340211b0c5e',
    
    class_name='SpatiallyFundamental',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f055e217_0b1b_4e7e_b8be_7340211b0c5e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpatiallyFundamental',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    