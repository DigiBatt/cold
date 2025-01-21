
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialTreatmentModule import MaterialTreatment







class Irradiate(MaterialTreatment):
    """
    Class representing the `Irradiate` entity, which inherits from:
    - MaterialTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c4fba898_896b_4d58_a24c_b5c0851fa2a2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Irradiate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Irradiate(
    
    class_iri='https://w3id.org/emmo#EMMO_c4fba898_896b_4d58_a24c_b5c0851fa2a2',
    
    class_name='Irradiate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c4fba898_896b_4d58_a24c_b5c0851fa2a2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Irradiate',
        alias="class_name"
    )
    

    
    

    

    