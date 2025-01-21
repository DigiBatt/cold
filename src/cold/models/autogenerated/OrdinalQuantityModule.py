
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuantityModule import Quantity







class OrdinalQuantity(Quantity):
    """
    Class representing the `OrdinalQuantity` entity, which inherits from:
    - Quantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c46f091c_0420_4c1a_af30_0a2c8ebcf7d7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OrdinalQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OrdinalQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_c46f091c_0420_4c1a_af30_0a2c8ebcf7d7',
    
    class_name='OrdinalQuantity',
    
    elucidation="example_value",
    
    example="example_value",
    
    VIMTerm="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c46f091c_0420_4c1a_af30_0a2c8ebcf7d7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OrdinalQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    

    
    

    

    