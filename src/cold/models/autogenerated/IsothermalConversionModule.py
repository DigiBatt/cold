
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HeatTreatmentModule import HeatTreatment







class IsothermalConversion(HeatTreatment):
    """
    Class representing the `IsothermalConversion` entity, which inherits from:
    - HeatTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6c213064_e525_45d4_99cf_afebed8bbddd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IsothermalConversion'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IsothermalConversion(
    
    class_iri='https://w3id.org/emmo#EMMO_6c213064_e525_45d4_99cf_afebed8bbddd',
    
    class_name='IsothermalConversion',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6c213064_e525_45d4_99cf_afebed8bbddd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IsothermalConversion',
        alias="class_name"
    )
    

    
    

    

    