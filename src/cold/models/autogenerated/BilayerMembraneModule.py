
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AsymmetricMembraneModule import AsymmetricMembrane







class BilayerMembrane(AsymmetricMembrane):
    """
    Class representing the `BilayerMembrane` entity, which inherits from:
    - AsymmetricMembrane

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f1c7eacb_9f21_4100_925c_3974f266e06f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BilayerMembrane'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BilayerMembrane(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f1c7eacb_9f21_4100_925c_3974f266e06f',
    
    class_name='BilayerMembrane',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f1c7eacb_9f21_4100_925c_3974f266e06f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BilayerMembrane',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    