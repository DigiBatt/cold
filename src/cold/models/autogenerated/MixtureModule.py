
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ContinuumSubstanceModule import ContinuumSubstance







class Mixture(ContinuumSubstance):
    """
    Class representing the `Mixture` entity, which inherits from:
    - ContinuumSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ec2c8ac8_98c5_4c74_b85b_ff8e8ca6655c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Mixture'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Mixture(
    
    class_iri='https://w3id.org/emmo#EMMO_ec2c8ac8_98c5_4c74_b85b_ff8e8ca6655c',
    
    class_name='Mixture',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ec2c8ac8_98c5_4c74_b85b_ff8e8ca6655c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Mixture',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    