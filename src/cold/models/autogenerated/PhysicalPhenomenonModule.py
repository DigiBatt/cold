
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProcessModule import Process







class PhysicalPhenomenon(Process):
    """
    Class representing the `PhysicalPhenomenon` entity, which inherits from:
    - Process

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_314d0bd5_67ed_437e_a609_36d46147cea7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicalPhenomenon'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicalPhenomenon(
    
    class_iri='https://w3id.org/emmo#EMMO_314d0bd5_67ed_437e_a609_36d46147cea7',
    
    class_name='PhysicalPhenomenon',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_314d0bd5_67ed_437e_a609_36d46147cea7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicalPhenomenon',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    