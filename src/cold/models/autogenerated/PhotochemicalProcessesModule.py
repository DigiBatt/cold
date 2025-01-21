
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialTreatmentModule import MaterialTreatment







class PhotochemicalProcesses(MaterialTreatment):
    """
    Class representing the `PhotochemicalProcesses` entity, which inherits from:
    - MaterialTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_00f2dc2d_2f64_468a_a77c_d70841b0b5f0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhotochemicalProcesses'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhotochemicalProcesses(
    
    class_iri='https://w3id.org/emmo#EMMO_00f2dc2d_2f64_468a_a77c_d70841b0b5f0',
    
    class_name='PhotochemicalProcesses',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_00f2dc2d_2f64_468a_a77c_d70841b0b5f0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhotochemicalProcesses',
        alias="class_name"
    )
    

    
    

    

    