
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialTreatmentModule import MaterialTreatment







class HeatTreatment(MaterialTreatment):
    """
    Class representing the `HeatTreatment` entity, which inherits from:
    - MaterialTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dacfc7dc_5ddb_4f67_986b_dcd01d649d60'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HeatTreatment'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HeatTreatment(
    
    class_iri='https://w3id.org/emmo#EMMO_dacfc7dc_5ddb_4f67_986b_dcd01d649d60',
    
    class_name='HeatTreatment',
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dacfc7dc_5ddb_4f67_986b_dcd01d649d60',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HeatTreatment',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    