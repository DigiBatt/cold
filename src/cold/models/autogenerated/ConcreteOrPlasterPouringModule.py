
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPulpModule import FormingFromPulp







class ConcreteOrPlasterPouring(FormingFromPulp):
    """
    Class representing the `ConcreteOrPlasterPouring` entity, which inherits from:
    - FormingFromPulp

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9e452535_a369_404d_9afb_d41fd79d12b8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConcreteOrPlasterPouring'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConcreteOrPlasterPouring(
    
    class_iri='https://w3id.org/emmo#EMMO_9e452535_a369_404d_9afb_d41fd79d12b8',
    
    class_name='ConcreteOrPlasterPouring',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9e452535_a369_404d_9afb_d41fd79d12b8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConcreteOrPlasterPouring',
        alias="class_name"
    )
    

    
    

    

    