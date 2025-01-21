
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalQuantityModule import PhysicalQuantity







class DerivedQuantity(PhysicalQuantity):
    """
    Class representing the `DerivedQuantity` entity, which inherits from:
    - PhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_71f6ab56_342c_484b_bbe0_de86b7367cb3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DerivedQuantity'`
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
    obj = DerivedQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_71f6ab56_342c_484b_bbe0_de86b7367cb3',
    
    class_name='DerivedQuantity',
    
    VIMTerm="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_71f6ab56_342c_484b_bbe0_de86b7367cb3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DerivedQuantity',
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
    

    
    

    

    